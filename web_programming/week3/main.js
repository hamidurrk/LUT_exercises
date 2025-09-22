document.addEventListener('DOMContentLoaded', async () => {
    try {
        const populationUrl = 'https://pxdata.stat.fi/PxWeb/api/v1/fi/StatFin/vaerak/statfin_vaerak_pxt_11ra.px';
        const employmentUrl = 'https://pxdata.stat.fi/PxWeb/api/v1/fi/StatFin/tyokay/statfin_tyokay_pxt_115b.px';

        console.log('Loading JSON queries...');
        const populationQuery = await fetch('population_query.json').then(response => {
            if (!response.ok) {
                throw new Error(`Failed to load population_query.json: ${response.status}`);
            }
            return response.json();
        });
        const employmentQuery = await fetch('employment_query.json').then(response => {
            if (!response.ok) {
                throw new Error(`Failed to load employment_query.json: ${response.status}`);
            }
            return response.json();
        });
        console.log('JSON queries loaded successfully');

        const [populationData, employmentData] = await Promise.all([
            fetch(populationUrl, {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(populationQuery)
            }).then(async response => {
                console.log('Population API response status:', response.status);
                const text = await response.text();
                console.log('Population API response text:', text.substring(0, 500));
                if (!response.ok) {
                    throw new Error(`Population API error: ${response.status} ${response.statusText}\nResponse: ${text}`);
                }
                return JSON.parse(text);
            }),
            fetch(employmentUrl, {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(employmentQuery)
            }).then(async response => {
                console.log('Employment API response status:', response.status);
                const text = await response.text();
                console.log('Employment API response text:', text.substring(0, 500));
                if (!response.ok) {
                    throw new Error(`Employment API error: ${response.status} ${response.statusText}\nResponse: ${text}`);
                }
                return JSON.parse(text);
            })
        ]);
        console.log('Data fetched successfully');

        console.log('Population data structure:', Object.keys(populationData));
        console.log('Employment data structure:', Object.keys(employmentData));

        const municipalities = populationData.dimension.Alue.category.label;
        const populations = populationData.value;
        const employments = employmentData.value;

        console.log('Processing', Object.keys(municipalities).length, 'municipalities');

        const tableBody = document.querySelector('#data-table tbody');

        for (const key in municipalities) {
            const municipality = municipalities[key];
            const population = populations[Object.keys(municipalities).indexOf(key)];
            const employment = employments[Object.keys(municipalities).indexOf(key)];
            const employmentPercentage = ((employment / population) * 100).toFixed(2);

            const row = document.createElement('tr');

            if (employmentPercentage > 45) {
                row.style.backgroundColor = '#abffbd';
            } else if (employmentPercentage < 25) {
                row.style.backgroundColor = '#ff9e9e';
            }

            row.innerHTML = `
                <td>${municipality}</td>
                <td>${population}</td>
                <td>${employment}</td>
                <td>${employmentPercentage}</td>
            `;

            tableBody.appendChild(row);
        }
        console.log('Table populated successfully');
    } catch (error) {
        console.error('Error loading data:', error);
        const tableBody = document.querySelector('#data-table tbody');
        tableBody.innerHTML = `<tr><td colspan="4">Error loading data: ${error.message}<br/>Please check the console for details.</td></tr>`;
    }
});

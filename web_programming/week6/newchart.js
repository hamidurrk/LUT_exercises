let birthsData = [];
let deathsData = [];
let chart;

const years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'];

async function fetchData(municipalityCode, dataType) {
    const requestBody = {
        "query": [
            {
                "code": "Vuosi",
                "selection": {
                    "filter": "item",
                    "values": years
                }
            },
            {
                "code": "Alue",
                "selection": {
                    "filter": "item",
                    "values": [municipalityCode]
                }
            },
            {
                "code": "Tiedot",
                "selection": {
                    "filter": "item",
                    "values": [dataType]
                }
            }
        ],
        "response": {
            "format": "json-stat2"
        }
    };

    try {
        const response = await fetch('https://statfin.stat.fi/PxWeb/api/v1/en/StatFin/synt/statfin_synt_pxt_12dy.px', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        return data.value || [];
    } catch (error) {
        console.error(`Error fetching ${dataType} data:`, error);
        return [];
    }
}

function createChart(births, deaths, title = 'Births & Deaths') {
    const chartData = {
        labels: years,
        datasets: [
            {
                name: 'Births',
                values: births,
                chartType: 'bar'
            },
            {
                name: 'Deaths',
                values: deaths,
                chartType: 'bar'
            }
        ]
    };

    const chartConfig = {
        title: title,
        data: chartData,
        type: 'bar',
        height: 450,
        colors: ['#63d0ff', '#363636'],
        axisOptions: {
            xAxisMode: 'tick'
        }
    };

    chart = new frappe.Chart('#chart', chartConfig);
}

async function init() {
    const municipalityCode = localStorage.getItem('currentMunicipality') || 'SSS';

    birthsData = await fetchData(municipalityCode, 'vm01');
    deathsData = await fetchData(municipalityCode, 'vm11');

    const municipalityName = municipalityCode === 'SSS' ? 'Whole Country' : 'Selected Municipality';
    createChart(birthsData, deathsData, `Births & Deaths - ${municipalityName}`);
}

document.addEventListener('DOMContentLoaded', init);
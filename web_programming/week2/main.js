document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submit-data").onclick = function(event) {
        event.preventDefault(); 

        var name = document.getElementById("input-username").value;
        var email = document.getElementById("input-email").value;
        var checkbox = document.getElementById("input-admin").checked;
        
        var imageFile = document.getElementById("input-image").files[0];

        var tableBody = document.getElementById("data-table").getElementsByTagName("tbody")[0];
        
        var usernames = [];
        for (var i = 0; i < tableBody.rows.length; i++) {
            usernames.push(tableBody.rows[i].cells[0].textContent);
        }
        if (usernames.includes(name)) {
            for (var i = 0; i < tableBody.rows.length; i++) {
                if (tableBody.rows[i].cells[0].textContent === name) {
                    tableBody.rows[i].cells[1].textContent = email;
                    tableBody.rows[i].cells[2].textContent = checkbox ? "X" : "-";
                    if (imageFile) {
                        var reader = new FileReader();
                        reader.onload = function(e) {
                            tableBody.rows[i].cells[3].innerHTML = '<img src="' + e.target.result + '" alt="User Image" width="64" height="64">';
                        };
                        reader.readAsDataURL(imageFile);
                    }
                    break;
                }
            }
        } else {
            var newRow = document.createElement("tr");

            var nameCell = document.createElement("td");
            nameCell.textContent = name;
            newRow.appendChild(nameCell);

            var emailCell = document.createElement("td");
            emailCell.textContent = email;
            newRow.appendChild(emailCell);

            var adminCell = document.createElement("td");
            adminCell.textContent = checkbox ? "X" : "-";
            newRow.appendChild(adminCell);

            var imageCell = document.createElement("td");
            if (imageFile) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    imageCell.innerHTML = '<img src="' + e.target.result + '" alt="User Image" width="64" height="64">';
                    newRow.appendChild(imageCell);
                    tableBody.appendChild(newRow);
                };
                reader.readAsDataURL(imageFile);
            } else {
                imageCell.innerHTML = '<img src="" alt="Placeholder Image" width="64" height="64">';
                newRow.appendChild(imageCell);
                tableBody.appendChild(newRow);
            }
        }
    };
    document.getElementById("empty-table").onclick = function() {
        var tableBody = document.getElementById("data-table").getElementsByTagName("tbody")[0];
        tableBody.innerHTML = "";
    };
});
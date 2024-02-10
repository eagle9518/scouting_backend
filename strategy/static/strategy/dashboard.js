document.getElementById("match_button").onclick = () => {
    let match = document.getElementById("match").value
    fetch("", {
        method: 'POST',
        credentials: 'include',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: (match)
    })
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data)
            let dashboardTable = document.getElementById("dashboardTable");
            for (let redTeam in data["red"]) {
                let redTeamRow = document.createElement("tr");
                for (let redTeamStat in data["red"][redTeam]) {
                    let redTeamData = document.createElement("td");
                    redTeamData.appendChild(document.createTextNode(data["red"][redTeam][redTeamStat]));
                    redTeamRow.appendChild(redTeamData);
                }
                dashboardTable.appendChild(redTeamRow);
            }
                // let redTeam = document.createElement("tr");
                // console.log(data["red"][redIndex])
                // for (let redTeamStatIndex = 0; redTeamStatIndex < Object.keys(data["red"][redIndex]).length; redTeamStatIndex++) {
                //     console.log(data["red"][redIndex][redTeamStatIndex]);
                //     let redTeamStat = document.createElement("td");
                //     redTeamStat.appendChild(document.createTextNode(data["red"][redIndex][redTeamStatIndex]));
                //     redTeam.appendChild(redTeamStat);
                //   }
                // dashboardTable.appendChild(redTeam);
                // }
        })
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const svgns = "http://www.w3.org/2000/svg";

const teamNumber = parseInt(document.currentScript.dataset.teamNumber)
const allTeamsInMatch = JSON.parse(document.currentScript.nextElementSibling.textContent);
const scoringGrid = JSON.parse(document.currentScript.nextElementSibling.nextElementSibling.textContent);
console.log(scoringGrid);
const scoringImage = document.getElementById("scoring-image");

for (let row = 0; row < 3; row++) {
    const tableData = document.createElement("td");
    if (allTeamsInMatch.slice(0, 3).includes(teamNumber)) {
        tableData.setAttribute("class", "red");
    } else {
        tableData.setAttribute("class", "blue");
    }

    const svg = document.createElementNS(svgns, "svg");
    svg.setAttribute("width", "24");
    svg.setAttribute("height", "216");
    svg.setAttribute("style", "display: block; margin: auto");

    let verticalOffset = 0;
    for (let col = 0; col < 9; col++) {
        let g = document.createElementNS(svgns, "g");
        g.setAttribute("transform", "translate(0, " + verticalOffset + ")");
        verticalOffset += 24;

        let rec = document.createElementNS(svgns, "rect");
        rec.setAttribute("x", "1");
        rec.setAttribute("y", "1");
        rec.setAttribute("width", "22");
        rec.setAttribute("height", "22");
        rec.setAttribute("rx", "4");
        console.log(scoringGrid[row + 3][col]);
        if (scoringGrid[row + 3][col] !== "0") {
            rec.setAttribute("style", "fill:rgb(0,255,0,0.3); stroke:rgb(0,0,0,0.2)");
        } else {
            rec.setAttribute("style", "fill:rgb(0,0,0,0); stroke:rgb(0,0,0,0.2)");
        }
        g.appendChild(rec);

        svg.appendChild(g);

    }

    tableData.appendChild(svg);
    scoringImage.appendChild(tableData);
}



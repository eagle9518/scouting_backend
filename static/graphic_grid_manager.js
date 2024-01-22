// SVG Namespace Website
const svgns = "http://www.w3.org/2000/svg";

// Get JSON data from backend
const teamNumber = parseInt(document.currentScript.dataset.teamNumber)
const allTeamsInMatch = JSON.parse(document.currentScript.nextElementSibling.textContent);
const scoringGrid = JSON.parse(document.currentScript.nextElementSibling.nextElementSibling.textContent);

const scoringImage = document.getElementById("scoring-image");

for (let row = 0; row < 6; row++) {
    scoringGrid[row] = JSON.parse("[" + scoringGrid[row] + "]");
}
console.log(scoringGrid);
// Traverse all three scoring grid rows
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

    let verticalOffset = 192;
    for (let col = 0; col < 9; col++) {
        let g = document.createElementNS(svgns, "g");
        g.setAttribute("transform", "translate(0, " + verticalOffset + ")");
        verticalOffset -= 24;

        let rec = document.createElementNS(svgns, "rect");
        rec.setAttribute("x", "1");
        rec.setAttribute("y", "1");
        rec.setAttribute("width", "22");
        rec.setAttribute("height", "22");
        rec.setAttribute("rx", "4");
        if (scoringGrid[row][col] !== 0) {
            rec.setAttribute("style", "fill:rgb(0,255,0,0.3); stroke:rgb(0,0,0,0.2)");
        } else {
            rec.setAttribute("style", "fill:rgb(0,0,0,0); stroke:rgb(0,0,0,0.2)");
        }
        g.appendChild(rec);

        let polygon = document.createElementNS(svgns, "polygon");
        if (scoringGrid[row][col] === 1 || scoringGrid[row + 3][col] === 1) {
            polygon.setAttribute("points", "12,5 8,20 5,20 19,20 16,20");
            polygon.setAttribute("style", "fill:rgb(255,200,0);stroke-width:1;stroke:rgb(0,0,0)")
        } else if (scoringGrid[row][col] === 2 || scoringGrid[row + 3][col] === 2) {
            polygon.setAttribute("points", "6,6 6,18 18,18 18,6");
            polygon.setAttribute("style", "fill:rgb(150,0,255);stroke-width:1;stroke:rgb(0,0,0)")
        }
        g.appendChild(polygon);

        svg.appendChild(g);
    }

    tableData.appendChild(svg);
    scoringImage.appendChild(tableData);
}



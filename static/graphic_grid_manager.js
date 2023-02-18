const relative_url = "/static/images/"
const grid_layout = [
    [{0: "grid_one_top_left_cone.png", 1: "grid_one_top_left_cone1.png"}, {0: "grid_one_top_cube.png", 2: "grid_one_top_cube2.png"}, {0: "grid_one_top_right_cone.png", 1: "grid_one_top_right_cone1.png"},
     {0: "grid_two_top_left_cone.png", 1: "grid_two_top_left_cone1.png"}, {0: "grid_two_top_cube.png", 2: "grid_two_top_cube2.png"}, {0: "grid_two_top_right_cone.png", 1: "grid_two_top_right_cone1.png"},
     {0: "grid_three_top_left_cone.png", 1: "grid_three_top_left_cone1.png"}, {0: "grid_three_top_cube.png", 2: "grid_three_top_cube2.png"}, {0: "grid_three_top_right_cone.png", 1: "grid_three_top_right_cone1.png"}],
    [{0: "grid_one_middle_left_cone.png", 1: "grid_one_middle_left_cone1.png"}, {0: "grid_one_middle_cube.png", 2: "grid_one_middle_cube2.png"}, {0: "grid_one_middle_right_cone.png", 1: "grid_one_middle_right_cone1.png"},
     {0: "grid_two_middle_left_cone.png", 1: "grid_two_middle_left_cone1.png"}, {0: "grid_two_middle_cube.png", 2: "grid_two_middle_cube2.png"}, {0: "grid_two_middle_right_cone.png", 1: "grid_two_middle_right_cone1.png"},
     {0: "grid_three_middle_left_cone.png", 1: "grid_three_middle_left_cone1.png"}, {0: "grid_three_middle_cube.png", 2: "grid_three_middle_cube2.png"}, {0: "grid_three_middle_right_cone.png", 1: "grid_three_middle_right_cone1.png"}],
    [{0: "grid_one_bottom_left_hybrid.png", 1: "grid_one_bottom_left_hybrid1.png", 2: "grid_one_bottom_left_hybrid2"}, {0: "grid_one_bottom_middle_hybrid.png", 1: "grid_one_bottom_middle_hybrid1.png", 2: "grid_one_bottom_middle_hybrid2"}, {0: "grid_one_bottom_right_hybrid.png", 1: "grid_one_bottom_right_hybrid1.png", 2: "grid_one_bottom_right_hybrid2"},
     {0: "grid_two_bottom_left_hybrid.png", 1: "grid_two_bottom_left_hybrid1.png", 2: "grid_two_bottom_left_hybrid2"}, {0: "grid_two_bottom_middle_hybrid.png", 1: "grid_two_bottom_middle_hybrid1.png", 2: "grid_two_bottom_middle_hybrid2"}, {0: "grid_two_bottom_right_hybrid.png", 1: "grid_two_bottom_right_hybrid1.png", 2: "grid_two_bottom_right_hybrid2"},
     {0: "grid_three_bottom_left_hybrid.png", 1: "grid_three_bottom_left_hybrid1.png", 2: "grid_three_bottom_left_hybrid2"}, {0: "grid_three_bottom_middle_hybrid.png", 1: "grid_three_bottom_middle_hybrid1.png", 2: "grid_three_bottom_middle_hybrid2"}, {0: "grid_three_bottom_right_hybrid.png", 1: "grid_three_bottom_right_hybrid1.png", 2: "grid_three_bottom_right_hybrid2"}]
];

const canvas = document.getElementById('auto_grid');
const context = canvas.getContext('2d');


function draw_grid() {
    let y = new Array(9).fill(0);
    for (let row = 0; row < grid_layout.length; row++) {
        let x = 0;
        for (let element = 0; element < grid_layout[row].length; element++) {
            let gridImage = new Image();
            gridImage.onload = () => {
                context.drawImage(gridImage, x, y[element]);
                x += gridImage.width;
                y[element] += gridImage.height;
            }
            gridImage.src = relative_url + grid_layout[row][element][0];
        }
    }
}

draw_grid();
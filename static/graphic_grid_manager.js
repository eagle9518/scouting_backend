const relative_url = "/static/images/"
const grid_layout = [
    [{0: "grid_one_top_left_cone.png", 1: "grid_one_top_left_cone1.png"}, {0: "grid_one_top_cube.png", 2: "grid_one_top_cube2.png"}, {0: "grid_one_top_right_cone.png", 1: "grid_one_top_right_cone1.png"},
     {0: "grid_two_top_left_cone.png", 1: "grid_two_top_left_cone1.png"}, {0: "grid_two_top_cube.png", 2: "grid_two_top_cube2.png"}, {0: "grid_two_top_right_cone.png", 1: "grid_two_top_right_cone1.png"},
     {0: "grid_three_top_left_cone.png", 1: "grid_three_top_left_cone1.png"}, {0: "grid_three_top_cube.png", 2: "grid_three_top_cube2.png"}, {0: "grid_three_top_right_cone.png", 1: "grid_three_top_right_cone1.png"}],
    [{0: "grid_one_middle_left_cone.png", 1: "grid_one_middle_left_cone1.png"}, {0: "grid_one_middle_cube.png", 2: "grid_one_middle_cube2.png"}, {0: "grid_one_middle_right_cone.png", 1: "grid_one_middle_right_cone1.png"},
     {0: "grid_two_middle_left_cone.png", 1: "grid_two_middle_left_cone1.png"}, {0: "grid_two_middle_cube.png", 2: "grid_two_middle_cube2.png"}, {0: "grid_two_middle_right_cone.png", 1: "grid_two_middle_right_cone1.png"},
     {0: "grid_three_middle_left_cone.png", 1: "grid_three_middle_left_cone1.png"}, {0: "grid_three_middle_cube.png", 2: "grid_three_middle_cube2.png"}, {0: "grid_three_middle_right_cone.png", 1: "grid_three_middle_right_cone1.png"}],
    [{0: "grid_one_bottom_left_hybrid.png", 1: "grid_one_bottom_left_hybrid1.png", 2: "grid_one_bottom_left_hybrid2.png"}, {0: "grid_one_bottom_middle_hybrid.png", 1: "grid_one_bottom_middle_hybrid1.png", 2: "grid_one_bottom_middle_hybrid2.png"}, {0: "grid_one_bottom_right_hybrid.png", 1: "grid_one_bottom_right_hybrid1.png", 2: "grid_one_bottom_right_hybrid2.png"},
     {0: "grid_two_bottom_left_hybrid.png", 1: "grid_two_bottom_left_hybrid1.png", 2: "grid_two_bottom_left_hybrid2.png"}, {0: "grid_two_bottom_middle_hybrid.png", 1: "grid_two_bottom_middle_hybrid1.png", 2: "grid_two_bottom_middle_hybrid2.png"}, {0: "grid_two_bottom_right_hybrid.png", 1: "grid_two_bottom_right_hybrid1.png", 2: "grid_two_bottom_right_hybrid2.png"},
     {0: "grid_three_bottom_left_hybrid.png", 1: "grid_three_bottom_left_hybrid1.png", 2: "grid_three_bottom_left_hybrid2.png"}, {0: "grid_three_bottom_middle_hybrid.png", 1: "grid_three_bottom_middle_hybrid1.png", 2: "grid_three_bottom_middle_hybrid2.png"}, {0: "grid_three_bottom_right_hybrid.png", 1: "grid_three_bottom_right_hybrid1.png", 2: "grid_three_bottom_right_hybrid2.png"}]
];

function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

function get_match_data_from_server() {
    return new Promise((resolve => {
        fetch("", {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: {"Match Data Wanted": 2073}
        })
            .then(response => {
                return response.json();
            })
            .then(data => {
                resolve(data["match_data"]);
            })
    }));

}


async function draw_grid(context, match_data) {
    let initial_x = 27;
    let y = new Array(9).fill(0);

    for (let row = 0; row < grid_layout.length; row++) {
        let x = (row !== 2) ? initial_x : 0;
        for (let element = 0; element < grid_layout[row].length; element++) {
            await new Promise((resolve) => {
                setTimeout(() => {
                    let grid_image = new Image();
                    grid_image.onload = () => {
                        context.drawImage(grid_image, x, y[element]);
                        x += grid_image.width;
                        y[element] += grid_image.height;
                    }
                    if (match_data[row][element] > 2 || match_data[row][element] === undefined) {
                        match_data[row][element] = 0;
                    }
                    grid_image.src = relative_url + grid_layout[row][element][match_data[row][element]];
                    resolve();
                }, 5);
            });
        }
    }
}

async function main() {
    const auto_canvas = document.getElementById('auto_grid');
    const auto_context = auto_canvas.getContext('2d');
    const teleop_canvas = document.getElementById('teleop_grid');
    const teleop_context = teleop_canvas.getContext('2d');

    let match_data = await get_match_data_from_server();

    draw_grid(auto_context, match_data).then();
    draw_grid(teleop_context, match_data).then();
}

main().then();



const cs = JSON.parse( document.querySelector(".cs").textContent );
const death = JSON.parse( document.querySelector(".death").textContent );
const time = JSON.parse( document.querySelector(".time").textContent );
const property = JSON.parse( document.querySelector(".property").textContent );


// chart 
for(let i = 0 ;i < cs.length ; i++){
    cs[i] /= time[i]   
}

const csCanvas = document.getElementById("cs-chart").getContext('2d');
var csGradient = csCanvas.createLinearGradient(0 , 0 , 0 , 200);
csGradient.addColorStop(0 , "rgba(58,123,213,1)");
csGradient.addColorStop(1 , 'rgba(0,210,255,1)' );

const deathCanvas = document.getElementById('death-chart').getContext('2d');
var deathGradient = deathCanvas.createLinearGradient(0 , 0 , 0 , 285);
deathGradient.addColorStop(0 , "#1abc9c");
deathGradient.addColorStop(1 , '#8e44ad' );


var csChart , deathChart;

function displayData( num_game )
{
    var labels = [];
    for(let i =  0 ; i < Math.max( cs.length , 7 ) ; i++){
        labels.push("");
    }
    
    console.log( num_game )
    cur_cs = []
    cur_death = []
    num_game = Math.min( num_game , cs.length )
    for(let i = cs.length - num_game; i < cs.length; i++){
        cur_cs.push( cs[i] );
        cur_death.push( death[i] );
    }

    const csData = {
        labels : labels,
        datasets : [
            {
                label : "CS",
                data : cur_cs,
                fill : true,
                backgroundColor : csGradient,
                pointBackgroundColor: 'rgba(58,123,213,1)',
                pointBorderColor : 'rgba(255,255,255,1)',
            }
        ]
    }

    const csConfig = {
        type : 'line',
        data : csData,
        options : {
            responsive : true,
            scales : {
                y : {
                    type : 'linear',
                    min : 0,
                    max : 10,
                    ticks : {
                        callback: function(val) {
                            return val + ' cs/m';
                        },
                    },
                }
            },
            maintainAspectRatio : false,
            plugins : {
                title : {
                    display : true,
                    text : 'CS Average: 5',
                }
            }
            
        },   
    }

    csChart = new Chart(
        csCanvas,
        csConfig,
    )

    const deathData = {
        labels : labels,
        datasets : [
            {
                label : "Death",
                data : cur_death,
                fill : true,
                backgroundColor : deathGradient,
                pointBackgroundColor: 'rgba(58,123,213,1)',
                pointBorderColor : 'rgba(255,255,255,1)',
            }
        ]
    }

    const deathConfig = {
        type : 'line',
        data : deathData,
        options : {
            responsive : true,
            scales : {
                y : {
                    type : 'linear',
                    min : 0,
                    max : 20,
                    ticks : {
                        callback: function(val) {
                            return val + ' d';
                        },
                    },
                }
            },
            maintainAspectRatio : false,
            plugins : {
                title : {
                    display : true,
                    text : 'Death Average: 5',
                }
            }
            
        },   
    }

    deathChart = new Chart(
        deathCanvas,
        deathConfig,
    )
}

displayData( cs.length )
// 

// total / win rate
const property_total_game = document.querySelectorAll(".property-box .info .total");
const property_win_rate = document.querySelectorAll(".property-box .info .win-rate");

for(let i = 0 ; i < property_total_game.length ; i++){
    property_total_game[i].textContent = property[i][0];   
    property_win_rate[i].textContent = property[i][1] + '%';
}

// add game

var addGame = document.querySelector(".add-game")
const addGameForm = document.querySelector(".add-game form")
const addGameButton = document.getElementById("add-game-button")

addGameButton.onclick = function() {
    addGame.classList.remove("inactive")
}

document.onclick = function(e) {
    if( e.target.id == "add-game-section" ) {
        addGame.classList.add("inactive")
    }
}

// display game

document.querySelectorAll(".num-game").forEach( (num_game) => {
    num_game.onclick = () => {
        let cur_num = parseInt( num_game.getAttribute("data-num") )
        deathChart.destroy()
        csChart.destroy()
        displayData(cur_num)
    }
})


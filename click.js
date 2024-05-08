var gameStartTime = performance.now(); //Jokoa hasterakoan denbora hasi
var clickCount = 0; //Klik kopurua kalkulatuko dugu ere
//var interactiveObjects = []; // Klikatutako botoi interaktiboak gordetzeko array-a

document.onmousedown = function (event) {
    var tempLink = document.createElement("a");

    if (!event) {
        event = window.event;
    }
	
	//Klik kopurua eguneratu
    clickCount++;
	
	//Arratoiaren X eta Y koordenatua lortu
    var mouseX = event.clientX; 
    var mouseY = event.clientY;
	
	//Jokoa hasi denetik pasatako denbora seguntuetan kalkulatu
    var currentTime = (performance.now() - gameStartTime) / 1000;
	
	//Erregistratu zein koordenatutan egin den klik
    console.log("Mousedown at: X=" + mouseX + ", Y=" + mouseY + " at time " + currentTime.toFixed(2) + " seconds");
	//Erregistratu uneko klik kopurua
	console.log("Click count: " + clickCount);
	// Erregistratu klik zein target-eri egin zaion
    console.log("Target Element:", event.target);
    // Erregistratu event osoa
    console.log("Event Object:", event);
	
	
};

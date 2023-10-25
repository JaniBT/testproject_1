const prompt = require("prompt-sync")();

let szam1 = prompt("Adj meg egy számot: ");
let szam2 = prompt("Adj meg egy másik számot: ");
let muvelet = prompt("Add meg, hogy milyen műveletet akarsz elvégezni (/,*,+,-): ");
const szamok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

if (szam1 != szamok && szam1 != szamok) {
  if (muvelet == "/") {
    let oszt = szam1 / szam2;
    console.log("Az eredmény: ", oszt);
  } else if (muvelet == "*") {
    let szoroz = szam1 * szam2;
    console.log("Az eredmény: ", szoroz);
  } else if (muvelet == "+") {
    let osszead = szam1 + szam2;
    console.log("Az eredmény: ", osszead);
  } else if (muvelet == "-") {
    let kivon = szam1 + szam2;
    console.log("Az eredmény: ", kivon);
  } else {
    console.log("Csak megadott műveleti jelet írhatsz be!");
  }
}
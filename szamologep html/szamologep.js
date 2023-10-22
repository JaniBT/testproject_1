function Szamologep () {
    const prompt = require("prompt-sync")();
    const elsoszam = prompt("Adj meg egy számot: ");
    const masodikszam = prompt("Adj meg még egy számot: ");
    const muveletijel = prompt("Add meg, hogy összeadni, kivonni, szorozni vagy osztani szeretnél (+, -, *, /): ");

    const osszeadas = elsoszam + masodikszam;
    const kivonas = elsoszam - masodikszam;
    const szoroz = elsoszam * masodikszam;
    const oszt = elsoszam / masodikszam;

    if (muveletijel == "+") {
        console.log("Az összeadás eredménye: ", osszeadas);
    } else if (muveletijel == "-") {
        console.log("A kivonás eredménye: ", kivonas);
    } else if (muveletijel == "*") {
        console.log("A szorzás eredménye: ", szoroz);
    } else if (muveletijel == "/") {
        console.log("Az osztás eredménye: ", oszt);
    } else {
        console.log("Csak ezeket a műveleti jeleket használhatod: (+, -, *, /)");
    }
}
Szamologep()
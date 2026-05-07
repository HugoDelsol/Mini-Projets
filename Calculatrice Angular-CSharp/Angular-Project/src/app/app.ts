import { Component, inject, signal, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Data } from './service/data'

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Angular-Project');
  private dataService = inject(Data);

  resultCalculate: any
  errorCalculate: any
  color: string = 'grey'
  isConnected: any

  buttons = [
    {id: 1, label: 'btn1', valeur: 1},
    {id: 2, label: 'btn2', valeur: 2},
    {id: 3, label: 'btn3', valeur: 3},
    {id: 4, label: 'btn4', valeur: 4},
    {id: 5, label: 'btn5', valeur: 5},
    {id: 6, label: 'btn6', valeur: 6},
    {id: 7, label: 'btn7', valeur: 7},
    {id: 8, label: 'btn8', valeur: 8},
    {id: 9, label: 'btn9', valeur: 9},
  ]

  testCalcul(valA: string, valB: string, o: string) {

    const a = parseFloat(valA);
    const b = parseFloat(valB);
    
    this.dataService.calculate(a, b, o).subscribe({
      next: (response) => {
        this.resultCalculate = response.result
        console.log("Resultat de calcul : ", response.result);
      },
      error: () => {
        this.resultCalculate = null;
        this.errorCalculate = "Veuillez entrez une valeur dans chaque inputs";
      }
    });
  }

  testGet() {
    this.dataService.testConnexion().subscribe({
      next: (response) => {
        this.color = "green";
        this.isConnected = "Connexion reussie"
        console.log(response);
      },
      error: (error) =>{ 
        this.color = "red";
        this.isConnected = "Connexion echouer"
        console.log(error)
      }
    });
  }

  variableSave(data: any) {
    console.log(data)
  }
}

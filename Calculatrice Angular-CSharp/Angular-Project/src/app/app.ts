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
}

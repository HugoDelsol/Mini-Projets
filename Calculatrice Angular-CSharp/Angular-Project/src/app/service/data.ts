import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})

export class Data {
  private http = inject(HttpClient);
  private apiUrlTest = 'http://localhost:5149/test';
  private apiUrlCalcul = 'http://localhost:5149/calculate';

  calculate(a: number, b: number, operation: string) {
    const body = { a, b, operation }
    return this.http.post<{result: number}>(this.apiUrlCalcul, body)
  }

  testConnexion() {    
    return this.http.get(this.apiUrlTest)
  }
}


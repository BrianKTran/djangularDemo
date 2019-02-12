import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  baseurl = "http://http://127.0.0.1:8000"
  httpHeaders = new HttpHeaders({'Content-type': 'application/json'})
  getExampleModel(): Observable<any>{
    return this.http.get(this.baseurl + '/movies/',
    {headers: this.httpHeaders});
  }
}

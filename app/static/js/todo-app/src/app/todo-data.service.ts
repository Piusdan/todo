import { Injectable } from '@angular/core';
import { Http, Response, Headers} from '@angular/http';
import {Observable} from 'rxjs/Rx';

import { Todo } from './todo';

@Injectable()
export class TodoDataService {
  private headers = new Headers();
  private baseUrl: string = '/api/v1.0/todos';
  private putUrl: string = '/api/v1.0/todos/complete';
  
  // my class constructor
  constructor(private http: Http) {
     this.headers.append('Content-Type', 'application/json');
   }

  // Simulate POST /todos
  // TODO
  addTodo(todo: Todo): Observable<TodoDataService> {
      return this.http.post(`${this.baseUrl}/$id`, {headers: this.headers})
            .map(this.extractData)
            .catch(this.handleError);
  }

  // Simulate DELETE /todos/:id
  // TODO
  deleteTodoById(id: number): Observable<TodoDataService> {
        return this.http.delete(`${this.baseUrl}/$id`, {headers: this.headers})
                  .map(this.extractData)
                  .catch(this.handleError);
  }

  // Simulate PUT /todos/:id
  // dont need this for now though
  updateTodoById(id: number): Observable<Todo> {
    return this.http.put(`${this.putUrl}/$id`, {headers: this.headers})
                  .map(this.extractData)
                  .catch(this.handleError);
  }

  // Simulate GET /todos
  getAllTodos(): Observable<Todo[]> {
    return this.http.get(this.baseUrl)
                  .map(this.extractData)
                  .catch(this.handleError);
  }

  // Simulate GET /todos/:id
  getTodoById(id: number): Observable<Todo> {
    return this.http.get(`${this.baseUrl}/$id`)
                  .map(this.extractData)
                  .catch(this.handleError);
  }

  // Simulate todo Complete
  toggleTodoComplete(todo: Todo){
      return this.http.put(`${this.putUrl}/$id`, {headers: this.headers})
                  .map(this.extractData)
                  .catch(this.handleError);
  }

  private extractData(res: Response) {
    let body = res.json();
    return body.data || { };
}
  private handleError (error: Response | any) {
      // In a real world app, you might use a remote logging infrastructure
      let errMsg: string;
      if (error instanceof Response) {
        const body = error.json() || '';
        const err = body.error || JSON.stringify(body);
        errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
      } else {
        errMsg = error.message ? error.message : error.toString();
      }
      console.error(errMsg);
      return Observable.throw(errMsg);
    }


}
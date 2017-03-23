import { Component } from '@angular/core';
import { Todo } from './todo'
import { TodoDataService } from './todo-data.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: []
})
export class AppComponent {

  newTodo: Todo = new Todo();
  // Ask Angular DI system to inject the dependancy
  // associated with the dependancy injection token `TodoDataService`
  // and assign it to a property called `todoDataService`
  constructor(private todoDataService: TodoDataService) {

  }
  
  // service is now availabele as this.todoDataService
  onToggleTodoComplete(todo) {
    this.todoDataService.toggleTodoComplete(todo)
  }

  onAddTodo(todo) {
    this.todoDataService.addTodo(todo);
  }

  onRemoveTodo(todo) {
    this.todoDataService.deleteTodoById(todo.id);
  }

  get todos() {
    return this.todoDataService.getAllTodos();
  }

}

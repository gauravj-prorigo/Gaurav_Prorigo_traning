<template>
  <div class="app">
    <h1>Simple Todo App</h1>

    <input v-model="newTodo" placeholder="Enter a task..." />
    <button @click="add">Add</button>


    <div class="actions" style="margin-top:12px;">
      <button class="delete-selected" @click="deleteSelected" :disabled="selectedCount === 0"
        title="Delete all checked tasks">
        Delete Selected ({{ selectedCount }})
      </button>
    </div>


    <ul style="margin-top:14px;">
      <li v-for="(todo, index) in todos" :key="index" :class="{ done: todo.done }">
        <div class="todo-item">
          <input type="checkbox" v-model="todo.done" @change="saveTodos" />
          <span>{{ todo.text }}</span>
        </div>
        <button @click="deletetodo(index)" class="delete-btn">
          <DeleteIcon />
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import DeleteIcon from 'vue-material-design-icons/Delete.vue';
export default {
  components: { DeleteIcon },
  name: "todo_list",
  data() {
    return {
      newTodo: "",
      todos: []

    };
  },
  computed: {
    selectedCount() {
      return this.todos.filter(t => t.done).length;
    }
  },
  methods: {
    add() {
      if (this.newTodo.trim() !== "") {
        this.todos.push({ text: this.newTodo, done: false });
        this.newTodo = "";
        this.saveTodos(); 
      }
    },
    deletetodo(index) {
      const ok = window.confirm("Are you sure you want to delete this task");
      if (ok) {
        this.todos.splice(index, 1);
        this.saveTodos();
        window.alert("Task Deleted");
      }
    },
    deleteSelected() {
      const count = this.selectedCount;
      if (count === 0) return;
      const ok = window.confirm(`Delete ${count} selected task(s)?`);
      if (!ok) return;
      this.todos = this.todos.filter(t => !t.done);
      this.saveTodos(); 
      window.alert(`${count} task(s) deleted`);
    },
    saveTodos() {
      localStorage.setItem("todos", JSON.stringify(this.todos));
    }
  },
  mounted() {
    const saved = localStorage.getItem("todos");
    if (saved) {
      this.todos = JSON.parse(saved);
    }
  }
};
</script>

<style scoped>
.app {
  max-width: 420px;
  margin: 40px auto;
  padding: 18px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
  text-align: center;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial;
}

input {
  padding: 8px;
  width: 70%;
  margin-right: 8px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

button {
  padding: 8px 12px;
  border: none;
  background-color: #3498db;
  color: white;
  border-radius: 6px;
  cursor: pointer;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.actions .delete-selected {
  background: #e74c3c;
  margin-left: 6px;
}

ul {
  list-style: none;
  padding: 0;
  margin-top: 12px;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8fbff;
  padding: 10px 12px;
  border-radius: 8px;
  margin-top: 8px;
}

.todo-item {
  display: flex;
  gap: 10px;
  align-items: center;
}

.delete-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 6px 8px;
  border-radius: 6px;
  cursor: pointer;
}

.done span {
  text-decoration: line-through;
  color: gray;
}
</style>
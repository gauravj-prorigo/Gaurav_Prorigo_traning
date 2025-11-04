<template>
  <div class="main">
    <div class="form-section">
      <h2>Simple Form</h2>
      <form @submit.prevent="submitForm" class="actual_form">
        <label>Name:</label>
        <input type="text" v-model="name" />

        <label>Email:</label>
        <input type="email" v-model="email" />

        <label>Message:</label>
        <textarea v-model="message"></textarea>

        <button type="submit">Submit</button>
      </form>

       <div class="display_form">
      <h3>Form Data:</h3>
      <p><strong>Name:</strong> {{ name }}</p>
      <p><strong>Email:</strong> {{ email }}</p>
      <p><strong>Message:</strong> {{ message }}</p>
    </div>
    </div>
<!-- 
   <div>
    <h1>Add list in bucket</h1>
    <label for="item">Add the items</label>
    <input type="text" name="list_items" id="" v-model="list_items">
    <button v-on:click="add">Add</button>

    <div class="bucket">
        <h2>List of items in bucket</h2>
          <ul>
      <li v-for="(item, index) in list" :key="index">{{ item }}</li>
    </ul>
    </div>
   </div> -->
  </div>
</template>

<script>
export default {
  name: "ContactForm",
  data() {
    return {
      name: "",
      email: "",
      message: "",
      list_items:"",
      list:[]
    };
  },
  methods: {
    submitForm() {
      alert(`Submitted:\nName: ${this.name}\nEmail: ${this.email}`);
    },
    add(){
           if (this.list_items.trim() !== "") {
        this.list.push(this.list_items);
        this.list_items = ""; // clear input box
      }
    }
  },
};
</script>

<style scoped>
.main {
  display: flex;
  gap: 50px; 
  align-items: flex-start;
  justify-content: center;
  margin-top: 40px;
  
}

.form-section,
.display_form {
  width: 35%;
  background: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
}

form {
  display: flex;
  flex-direction: column;
}

input,
textarea {
  justify-content: center;
    margin: 0 auto 10px auto;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 70%;
}

button {
  width: 50%;  
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px;
  border-radius: 5px;
  cursor: pointer;
  margin: auto;
}

button:hover {
  background-color: #0056b3;
}



.bucket h2 {
  color: #42b983; 
  margin-bottom: 15px;
}

.bucket ul {
  list-style-type: none; 
  padding: 0;
}

.bucket li {
  font-weight: 400;
  margin-bottom: 8px;
  padding: 8px 10px;
 

}

</style>

<script setup>
import { ref } from "vue";
import "@/assets/bootstrap.css";

const username = ref("");
const password = ref("");

async function login(_) {
  console.log(username.value, password.value);
  await fetch('http://localhost:8080/login', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username.value, password: password.value
    }),
  });
}

</script>

<template>
  <div class="container-sm mt-5">
    <h1 class="display-3">User Login</h1>
    <form @submit.prevent="login">
      <div class="row mb-3 align-center">
        <label class="col-auto align-self-center">
          Username
        </label>
        <input v-model="username" placeholder="username" class="form-control col" />
      </div>

      <div class="row mb-3">
        <label class="col-auto  align-self-center">
          Password
        </label>
        <input type="password" v-model="password" placeholder="password" class="form-control col" />
      </div>

      <div class="row">
        <input type="submit" value="login" class="btn btn-primary" />
      </div>
    </form>
  </div>
</template>

<style scoped>
label {
  font-size: large;
  ;
}
</style>
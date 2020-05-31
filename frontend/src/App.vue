<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <h2><a href="/">Serverless URL Shortner</a></h2>
      </div>
      <v-spacer></v-spacer>
      <v-btn href="https://github.com/pubudusj" target="_blank" text>
        <span class="mr-2">Github</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<style scoped>
.v-application a {
  color: white;
  text-decoration: none;
}
</style>

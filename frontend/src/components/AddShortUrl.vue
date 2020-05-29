<template>
  <v-container>
    <h2 class="title">Create New Short URL</h2>
    <v-alert v-if="alertText" outlined :type="valertType" text>
      {{ alertText }}
    </v-alert>
    <v-row align="center">
      <v-col cols="12">
        <v-form ref="form" class="my-3">
          <v-text-field
            v-model="url"
            label="Long URL to be shorten"
            required
          ></v-text-field>
          <p v-if="error" class="validation-error">{{ error }}</p>
          <v-btn
            color="success"
            class="mr-4"
            @click="validate"
          >
            Submit
          </v-btn>

          <v-btn color="error" class="mr-4" @click="reset">
            Reset
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import store from "../store/index";
export default {
  data: () => ({
    alertText: "",
    valertType: "success",
    overlay: false,
    url: "",
    error: false,
  }),

  methods: {
    validate() {
      if (! this.url) {
        this.error = 'URL is required.';
      } else if (! this.isAUrl(this.url)) {
        this.error = 'Invalid URL.';
      } else {
        this.addShortUrl();
      }
    },
    reset() {
      this.error = false
      this.$refs.form.reset();
      this.showAlert = false;
    },
    async addShortUrl() {
      this.overlay = true;
      await store.dispatch("addShortUrl", {
        url: this.url,
      });
      this.overlay = false;
      this.$refs.form.reset();
      this.alertText = "Short url added successfully.";
    },
    isAUrl(str) {
      var pattern = new RegExp(
        "^(https?:\\/\\/)?" + // protocol
        "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
        "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
        "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
        "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
          "(\\#[-a-z\\d_]*)?$",
        "i"
      ); // fragment locator
      return !!pattern.test(str);
    },
  },
};
</script>

<style scoped>
.title {
  margin-bottom: 10px;
}
.validation-error {
  color: red;
}
</style>

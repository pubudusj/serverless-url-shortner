<template>
  <v-container>
    <h2 class="title">Create New Short URL</h2>
    <v-alert
      v-if="alertText"
      outlined
      :type="valertType"
      text
    >
    {{ alertText }}
    </v-alert>
    <v-row align="center">
      <v-col cols="12">
        <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    class="my-3"
  >
    <v-text-field
      v-model="url"
      :rules="urlRules"
      label="Long URL to be shorten"
      required
    ></v-text-field>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Submit
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset
    </v-btn>
  </v-form>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import store from '../store/index'
  export default {
    data: () => ({
      alertText: '',
      valertType: 'success',
      overlay: false,
      valid: true,
      url: '',
      urlRules: [
        v => !!v || 'URL is required',
        // v => !!this.validURL(v) || 'URL must be valid',
      ],
    }),

    methods: {
      validate () {
        if(this.$refs.form.validate() === true) {
          this.addShortUrl()
        }
      },
      reset () {
        this.$refs.form.reset()
        this.showAlert = false;
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
      async addShortUrl() {
        this.overlay = true
        await store.dispatch('addShortUrl', {
          url: this.url
        })
        this.overlay = false
        this.$refs.form.reset()
        this.alertText = 'Short url added successfully.';
      },
      validURL(str) {
        var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
          '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
          '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
          '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
          '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
          '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
        return !!pattern.test(str);
      }
    }
  }
</script>

<style scoped>
  .title {
    margin-bottom: 10px;
  }
</style>
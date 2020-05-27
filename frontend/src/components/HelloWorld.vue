<template>
  <v-container>
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
  export default {
    data: () => ({
      valid: true,
      url: '',
      urlRules: [
        v => !!v || 'URL is required',
        v => /.+@.+\..+/.test(v) || 'URL must be valid',
      ],
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
  }
</script>
<template>
  <v-container>
    <h2>Usage of short URL : {{ short_code }}</h2>
  </v-container>
</template>

<script>
  import { mapState, mapGetters, mapActions } from 'vuex'

  export default {
    name: 'ListVisits',

    data () {
      return {
        short_url_base_path: process.env.VUE_APP_SHORT_URL_BASE_PATH,
        short_code: this.$route.params.short_code
      }
    },
    methods:{
      // fetchVisits(){
      //   this.$store.dispatch('fetchVisits', '')
      // }
    },
    mounted() {
      // this.fetchVisits()
    },
    computed: {
      ...mapState(['short_urls', 'loader']),
      ...mapGetters(['getShortUrls']),
      ...mapActions(['fetchShortUrls']),
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }
</style>
<template>
  <v-container>
    <h2>Short URLs</h2>
    <v-simple-table v-if="short_urls">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">URL</th>
            <th class="text-left">Short URL</th>
            <th class="text-left"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="short_urls.length == 0">
            <td colspan="2">No items found.</td>
          </tr>
          <tr v-for="item in short_urls" :key="item.name">
            <td>{{ item.url }}</td>
            <td><a target="_blank" :href="short_url_base_path + item.short_code">{{ item.short_code }}</a></td>
            <td><router-link :to="{ name: 'Stats', params: { short_code: item.short_code }}">Stats > </router-link></td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-container>
</template>

<script>
  import { mapState, mapGetters, mapActions } from 'vuex'

  export default {
    name: 'ListShortUrls',

    data () {
      return {
        short_url_base_path: process.env.VUE_APP_API_BASE_URL + 's/'
      }
    },
    methods:{
      fetchUrls(){
        this.$store.dispatch('fetchShortUrls')
      }
    },
    mounted() {
      this.fetchUrls()
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
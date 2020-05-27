<template>
<v-container>
      <v-overlay :value="loader">
        <v-progress-circular indeterminate size="64">{{ loader }}</v-progress-circular>
      </v-overlay>
      <AddShortUrl />
      <ListShortUrls />
</v-container>
</template>

<script>
import AddShortUrl from '@/components/AddShortUrl.vue'
import ListShortUrls from '@/components/ListShortUrls.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    AddShortUrl,
    ListShortUrls
  },
  computed: {
      ...mapState(['loader']),
    }
}
</script>

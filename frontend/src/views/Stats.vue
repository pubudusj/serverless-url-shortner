<template>
<v-container>
      <v-overlay :value="loader">
        <v-progress-circular indeterminate size="64">{{ loader }}</v-progress-circular>
      </v-overlay>
      <ListVisits />
</v-container>
</template>

<script>
import ListVisits from '@/components/ListVisits.vue'
import { mapState } from 'vuex'

export default {
  name: 'Stats',
  components: {
    ListVisits,
  },
  computed: {
      ...mapState(['loader']),
    }
}
</script>

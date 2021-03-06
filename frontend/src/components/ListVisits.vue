<template>
  <v-container>
    <h2>Usage of short URL : {{ short_code }}</h2>
    <h3 class="count" v-if="total_visits">Total visits: {{ total_visits }}</h3>
    <div v-show="total_visits">
      <div ref="chartdiv" id="chartdiv" style="width: 100%; height: 400px;"></div>
    </div>
    <v-alert class="banner" v-if="total_visits == 0" outlined type="warning" text>
      No statistics found.
    </v-alert>
  </v-container>
</template>

<script>
  import { mapActions } from 'vuex'
  import * as am4core from "@amcharts/amcharts4/core";
  import * as am4charts from "@amcharts/amcharts4/charts";
  import am4themes_animated from "@amcharts/amcharts4/themes/animated";
  
  am4core.useTheme(am4themes_animated);

  export default {
    name: 'ListVisits',

    data () {
      return {
        short_code: this.$route.params.short_code,
        chart_data: [],
        total_visits: null
      }
    },

    methods:{
      fetchStats(){
        let self = this
        this.$store.dispatch('fetchStats', this.short_code)
          .then(function(data) {
            self.total_visits = data.total_count

            // Arrange dates in between
            let getAllDates = self.getDatesBetweenDates(Object.keys(data.stats)[0], Object.keys(data.stats)[Object.keys(data.stats).length - 1])
            for (var i in getAllDates) {
              let chartDate = getAllDates[i].toISOString().substring(0, 10)
              if (chartDate in data.stats == true) {
                self.chart_data.push(
                  { "date": chartDate, "count": data.stats[chartDate] }
                )
              } else {
                self.chart_data.push(
                  { "date": chartDate, "count": 0 }
                )
              }
            }

            for (var prop in data.stats) {
              self.chart_data.push(
                { "date": prop, "count": data.stats[prop] }
              )
            }

            self.drawChart()
          })
      },
      drawChart() {
        let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart)
        chart.data = this.chart_data

        var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
        categoryAxis.renderer.grid.template.location = 0;
        categoryAxis.dataFields.category = "date";

        var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
        valueAxis.min = 0;
        valueAxis.strictMinMax = true;
        valueAxis.renderer.minGridDistance = 30;

        var series = chart.series.push(new am4charts.ColumnSeries());
        series.dataFields.categoryX = "date";
        series.dataFields.valueY = "count";
        series.columns.template.tooltipText = "{valueY.value}";
        series.columns.template.tooltipY = 0;
        series.columns.template.strokeOpacity = 0;
        
        this.chart = chart
      },
      getDatesBetweenDates(startDate, endDate) {
        let dates = []
        const theDate = new Date(startDate)
        while (theDate < new Date(endDate)) {
          dates = [...dates, new Date(theDate)]
          theDate.setDate(theDate.getDate() + 1)
        }
        dates = [...dates, new Date(endDate)]

        return dates
      }
    },
    mounted() {
      this.fetchStats()
    },
    computed: {
      ...mapActions(['fetchVisits']),
    },
    beforeDestroy() {
      if (this.chart) {
        this.chart.dispose();
      }
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }

  .count {
    margin-bottom: 40px;
  }

  .banner {
    margin-top: 40px;
  }
</style>
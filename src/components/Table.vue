<template>
  <br> 
  <div class="center-justified">
  <p> The below table lists the suspicious transaction loops that have all occurred
        within a 7-day period. The chance that these loops would occur naturally is negligible,
        thus it is strong evidence that these transactions are between either the same person
        e.g., the same person has several wallets to wash trade, or individuals are
        partnering to increase volume of transactions. <br> <br> 
        These transactions have the effect of artificially increasing liquidity within these collections.
        Strikingly cool cats, doodles, penguin and clonex exhibit over 40 - 70% of their wash trade activity in the
       first month. This indicates coordinated wash trading within the early days of a collection day being launched
        to build hype. It is notable that in loops when a collection is more mature, prices tend to be higher than
        our predicted value would expect. This is particularly the case for crypto punks. <br> <br>
        Use the table to search a transaction you are interested in. Clicking on from and to address will take
        you to the relevant Opensea account, and clicking the transaction hash will take you to etherscan.io record <br></p>
  </div>
  <div class="search" style="text-align: left">
    <label>Search:</label><input v-model="searchTerm" />
  </div>
  <table-lite
    :has-checkbox="true"
    :is-loading="table.isLoading"
    :is-re-search="table.isReSearch"
    :columns="table.columns"
    :rows="table.rows"
    :total="table.totalRecordCount"
    :sortable="table.sortable"
    :messages="table.messages"
    @do-search="doSearch"
    @is-finished="tableLoadingFinish"
  ></table-lite>
</template>

<script>
import { text } from "body-parser";
import { defineComponent, reactive, computed, ref } from "vue";
import TableLite from "vue3-table-lite";
import test from '../../public/table_data/table_data.json'

const sampleData1 = (offst, limit) => {
    let data = [];
    for (let i = offst; i < limit; i++) {
      data.push(test[i]);
    }
    return data;
};

export default defineComponent({
  name: 'App',
  components: {
    TableLite,
  },
  setup() {
    //  Table
    const searchTerm = ref(""); 
    const table = reactive({
      isLoading: false,
      isReSearch: false,
      columns: [
        {
          label: "Loop ID",
          field: "loopid",
          width: "10%",
          isKey: true,
        },
        {
          label: "From Address",
          field: "fromaddress",
          width: "10%",
          display: function (row) {
              var tempLabel = row.fromaddress.replaceAll("_", ".")
            return (
              '<a href="https://opensea.io/' + tempLabel + '" data-id="'
                + '" class="name-btn">' +
              tempLabel.substring(0, 10) + '...' +
              "</button>"
            );
        },
        },
        {
          label: "To Address",
          field: "toaddress",
          width: "10%",
          display: function (row) {
              var tempLabel = row.toaddress.replaceAll("_", ".")
            return (
              '<a href="https://opensea.io/' + tempLabel + '" data-id="'
                + '" class="name-btn">' +
              tempLabel.substring(0, 10) + '...' +
              "</button>"
            );
          }
        },
        {
          label: "Token ID",
          field: "tokenid",
          width: "10%",
          sortable: true,
        },
        {
          label: "ETH Price",
          field: "ethprice",
          width: "10%",
          sortable: true,
        },
        {
          label: "Date",
          field: "date",
          width: "10%",
          sortable: true,
        },
        {
          label: "Transaction Hash",
          field: "transhash",
          width: "10%",
          display: function (row) {
            return (
              '<a href="https://etherscan.io/tx/' + row.transhash + '" data-id="'
                + '" class="name-btn">' +
              row.transhash.substring(0, 10) + '...' +
              "</button>"
            );
          }
        }
      ],
      //rows: sampleData1(0, 1096),
      rows: computed(() => {
        return sampleData1(0, 1096).filter(
          (x) =>
            x.loopid.toLowerCase().includes(searchTerm.value.toLowerCase())
        );
      }),
      totalRecordCount: 1096,
      sortable: {
        order: "id",
        sort: "asc",
      },
      messages: {
        pagingInfo: "Showing {0}-{1} of {2}",
        pageSizeChangeLabel: "Row count:",
        gotoPageLabel: "Go to page:",
        noDataAvailable: "No data",
      },
    });
    const doSearch = (offset, limit, order, sort) => {
      table.isLoading = true;
      setTimeout(() => {
        table.isReSearch = offset === undefined ? true : false;
        if (limit >= 20) {
          limit = 20;
        }
        if (sort === "asc") {
          table.rows = sampleData1(offset, limit);
        } else {
          table.rows = sampleData2(offset, limit);
        }
        table.totalRecordCount = 20;
        table.sortable.order = order;
        table.sortable.sort = sort;
      }, 600);
    };
    /**
     *
     * @param Collection elements 
     */
    const tableLoadingFinish = (elements) => {
      table.isLoading = false;
      Array.prototype.forEach.call(elements, function (element) {
        if (element.classList.contains("name-btn")) {
          element.addEventListener("click", function () {
          });
        }
        if (element.classList.contains("quick-btn")) {
          element.addEventListener("click", function () {
          });
        }
      });
    };
    return {
      table,
      doSearch,
      searchTerm,
      tableLoadingFinish
    };
  },
});
</script>

<style>
#app {
  font-family: Avenir;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.search {
    font-size: 30px;
    font-family: Avenir;
    color: black;
}
.center-justified {
  text-align: justify;
  margin: 0 auto;
  width: 40em;
}
</style>
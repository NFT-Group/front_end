<template>
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
import { defineComponent, reactive } from "vue";
import TableLite from "vue3-table-lite";
import test from '../../public/table_data/table_data.json'

const sampleData1 = (offst, limit) => {
    console.log(test[0])
    offst = offst + 1;
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
    const table = reactive({
      isLoading: false,
      isReSearch: false,
      columns: [
        {
          label: "Loop ID",
          field: "loopid",
          width: "14%",
          sortable: true,
          isKey: true,
        },
        {
          label: "From Address",
          field: "fromaddress",
          width: "14%",
          sortable: true,
          display: function (row) {
            return (
              '<a href="https://etherscan.io/address/' + row.fromaddress + '" data-id="'
                + '" class="name-btn">' +
              row.fromaddress.substring(0, 10) + '...' +
              "</button>"
            );
        },
        },
        {
          label: "To Address",
          field: "toaddress",
          width: "14%",
          sortable: true,
          display: function (row) {
            return (
              '<a href="https://etherscan.io/address/' + row.toaddress + '" data-id="'
                + '" class="name-btn">' +
              row.toaddress.substring(0, 10) + '...' +
              "</button>"
            );
          }
        },
        {
          label: "Token ID",
          field: "tokenid",
          width: "14%",
        },
        {
          label: "ETH Price",
          field: "ethprice",
          width: "14%",
        },
        {
          label: "Date",
          field: "date",
          width: "14%",
        },
        {
          label: "Transaction Hash",
          field: "transhash",
          width: "14%",
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
      rows: sampleData1(0, 1096),
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
            console.log(this.dataset.id + " name-btn click!!");
          });
        }
        if (element.classList.contains("quick-btn")) {
          element.addEventListener("click", function () {
            console.log(this.dataset.id + " quick-btn click!!");
          });
        }
      });
    };
    return {
      table,
      doSearch,
      tableLoadingFinish
    };
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
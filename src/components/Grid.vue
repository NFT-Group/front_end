<template>
    <div class="wrapper">
    <form id="search">
        Search <input name="query" v-model="searchQuery">
    </form>
    <div id="grid-template">
        <div class="table-header-wrapper">
        <table class="table-header">
            <thead>
            <th v-for="key in columns"
                @click="sortBy(key)"
                :class="{ active: sortKey == key }">
                {{ key }}
                <span class="arrow" :class="sortOrders[key] > 0 ? 'asc' : 'dsc'"></span>
            </th>
            </thead>
        </table>
        </div>
        <div class="table-body-wrapper">
        <table class="table-body">
            <tbody>
            <tr v-for="entry in filteredData">
                <td v-for="key in columns"> {{entry[key]}}</td>
            </tr>
            </tbody>
        </table>
        </div>
    </div>
    </div>
</template> 

<script>
    export default {
    name: "grid",
    props: {
        data: Array,
        columns: Array,
    },
    data(){
        return {
        searchQuery: '',
        sortKey: '',
        sortOrders: {},
        }
    },
    computed: {
        filteredData: function () {
        let sortKey = this.sortKey;
        let filterKey = this.searchQuery && this.searchQuery.toLowerCase();
        let order = this.sortOrders[sortKey] || 1;
        let data = this.data;

        if (filterKey) {
            data = data.filter(function (row) {
            return Object.keys(row).some(function (key) {
                return String(row[key]).toLowerCase().indexOf(filterKey) > -1;
            })
            })
        }
        if (sortKey) {
            data = data.slice().sort(function (a, b) {
            a = a[sortKey];
            b = b[sortKey];
            return (a === b ? 0 : a > b ? 1 : -1) * order;
            })
        }
        return data;
        },
    },
    methods: {
        sortBy: function (key) {
        this.sortKey = key;
        this.sortOrders[key] = this.sortOrders[key] * -1
        },
    },
    created(){
        let sortOrders = {};
        this.columns.forEach(function (key) {
        sortOrders[key] = 1;
        })
        this.sortOrders = sortOrders;
    }
    }
</script>


<style>
    body{
    font-size: 14px;
    color: #555;
    }

    table {
    border-spacing: 0;
    width: 100%;
    /* justify-content: center; */

    }

    th {
    background-color:midnightblue;
    color: rgba(255,255,255,0.66);
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    td {
    border-bottom: 1px #2c3e50 solid;
    }

    th, td {
    min-width: 150px;
    padding: 10px 20px;
    }

    th.active {
    color: #fff;
    }

    th.active .arrow {
    opacity: 1;
    }

    .arrow {
    display: inline-block;
    vertical-align: middle;
    width: 0;
    height: 0;
    margin-left: 5px;
    opacity: 0.66;
    }

    .arrow.asc {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 4px solid white;
    }

    .arrow.dsc {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid white;
    }

    #grid-template {
    display: flex;
    display: -webkit-flex;
    flex-direction: column;
    -webkit-flex-direction: column;
    /* width: 1600px; */
    align-items: center;
    justify-content: center;
    }
</style>
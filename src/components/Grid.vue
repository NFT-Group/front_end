<template>
    <div class="wrapper">
    <form @submit="onSubmit2">
      <label>Choose a Collection:</label>
        <select value="collection" id="collection" name="collection">
            <option value="Crypto Punks" id="Crypto Punks" name="collection">CryptoPunks</option>
            <option value="Bored Ape Yacht Club" id="Bored Ape Yacht Club" name="collection" selected="selected">Bored Ape Yacht Club</option>
            <option value="Bored Ape Kennel Club" id="Bored Ape Kennel Club" name="collection">Bored Ape Kennel Club</option>
            <option value="Doodles" id="Doodles" name="collection">Doodles</option>
            <option value="Cryptoadz" id="Cryptoadz" name="collection">CrypToadz</option>
            <option value="Pudgy Penguins" id="Pudgy Penguins" name="collection">Pudgy Penguins</option>
            <option value="Cool Cats" id="Cool Cats" name="collection">Cool Cats</option>
            <option value="Clonex" id="Clonex" name="collection">cloneX</option>
        </select>
        <br><br>
        <input type="submit" name="submit_button2">
    </form>
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
        sortOrders: {}
        }
    },
    computed: {
        filteredData() {
            // console.log("Being called now")
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
        onSubmit2(evt) {
                // Refresh SVG 
                evt.preventDefault();
                var collection_name = evt.srcElement.collection.value
                // Render node chart
                filteredData(collection_name)
        },
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
    width: 50%;
    /* justify-content: center; */
    color: black;
    }
    th {
    background-color:#666e77;
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
    min-width: 120px;
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
    color: black;
    }
</style>
<template>
    <div class="entries-container">
        <div v-for="(entry, id) in getContent" :key="id">
            <h3>Name: {{entry.Name}}</h3>
            <h5>E Mail: {{entry["E-mail"]}}</h5>
            <h5>URL: {{entry["URL"]}}</h5>
        </div>
    </div>
</template>

<script>
export default {
    name: "Entries",
    data() {
        return {
            upstreamBase: "http://localhost:5000/",
            fetchedEntries: null
        }
    },
    methods: {
        fetchUpstream: async function() {
            const response = await fetch(this.upstreamBase);
            const jsonData = await response.json();

            this.fetchedEntries = jsonData;
        }
    },
    computed: {
        getContent() {
            return this.fetchedEntries;
        }
    },
    mounted() {
        this.fetchUpstream();
    }
}
</script>
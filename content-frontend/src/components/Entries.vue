<template>
    <div class="entries-container">
        <div v-for="(entry, id) in getContent" :key="id">
            <h4>Name: {{entry.Name}}</h4>
            <h5>
                <span>E Mail: {{entry["E-mail"]}}</span>
                <span> URL: {{entry["URL"]}}</span>
                <span> Tags: {{entry["Tags"]}}</span>
            </h5>
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
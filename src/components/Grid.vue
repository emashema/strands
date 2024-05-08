<template>
    <div class="container px-0">

        <connection
            :x1="0"
            :y1="0"
            :x2="50"
            :y2="50"
        />

        <b-row
            v-for="(row, i) in board"
            :key="i"
            no-gutters
            class="mb-2"
        >
            <b-col
                v-for="(col, j) in row"
                :key="j"
            >
                <letter
                    :letter="board[i][j]"
                    @click="click"
                />
            </b-col>
        </b-row>
    </div>
</template>

<script>
import Letter from './Letter.vue'
import Connection from './Connection.vue'

export default {
    components: {
        Letter,
        Connection
    },
    props: {
        "board"             : { type: Array, required: true },
        "clue"              : { type: String, required: true },
        "spangram"          : { type: String, required: true },
        "strands"           : { type: Array, required: true },
        "strand_coordinates": { type: Array, required: true },
        "words"             : { type: Array, required: true },
    },
    data() {
        return {
            lines: [],
            attempt: []
        }
    },
    methods: {
        click() {
            // TODO
        }
    }
}
</script>
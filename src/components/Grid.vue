<template>
    <div class="container px-0">
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
                />
            </b-col>
        </b-row>
    </div>
</template>

<script>
import Letter from './Letter.vue'

export default {
    components: {
        Letter
    },
    props: {
        "board"             : { type: Array, required: true },
        "clue"              : { type: String, required: true },
        "spangram"          : { type: String, required: true },
        "strands"           : { type: Array, required: true },
        "strand_coordinates": { type: Array, required: true },
        "words"             : { type: Array, required: true },
    }
}
</script>
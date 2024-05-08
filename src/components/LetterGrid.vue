<template>
    <div class="container px-0">

        <letter-line
            v-for="line in lines"
            :key="line.x1+'-'+line.y1+'-'+line.x2+'-'+line.y2"
            :x1="line.x1"
            :y1="line.y1"
            :x2="line.x2"
            :y2="line.y2"
        />

        <b-row
            v-for="(row, x) in board"
            :key="x"
            no-gutters
            class="mb-2"
        >
            <b-col
                v-for="(col, y) in row"
                :key="y"
            >
                <letter
                    :letter="board[x][y]"
                    @click="click(board[x][y], x, y)"
                />
            </b-col>
        </b-row>
    </div>
</template>

<script>
import Letter from './Letter.vue'
import LetterLine from './LetterLine.vue'

export default {
    components: {
        Letter,
        LetterLine
    },
    props: {
        "board"             : { type: Array, required: true },
        "clue"              : { type: String, required: true },
        "spangram"          : { type: String, required: true },
        "strands"           : { type: Array, required: true },
        "strand_coordinates": { type: Object, required: true },
        "words"             : { type: Array, required: true },
    },
    data() {
        return {
            attempt: [
                // [ E
                //     5,
                //     5
                // ],
                // [ N
                //     6,
                //     5
                // ],
                // [ V
                //     7,
                //     5
                // ],
                // [ Y
                //     6,
                //     4
                // ]
            ]
        }
    },
    computed: {
        lines() {
            let l = []

            console.log('> in LINES')
            console.log(this.attempt.length)
            for (let index = 0; index < this.attempt.length-1; index++) {
                l.push(
                    {
                        x1: this.attempt[index][1],
                        y1: this.attempt[index][0],
                        x2: this.attempt[index+1][1],
                        y2: this.attempt[index+1][0]
                    }
                )
            }

            console.log(JSON.stringify(l))

            return l
        }
    },
    methods: {
        click(letter, x, y) {
            // console.log(letter)
            // console.log(x)
            // console.log(y)
            // TODO - push only if valid attempt([3,3] => [[2,2],[2,3],[2,4],[3,4],[4,4],[4,3],[4,2],[3,2]])
            this.attempt.push([x, y])
            // console.log(JSON.stringify(this.attempt))
        }
    }
}
</script>
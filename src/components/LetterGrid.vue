<template>
    <div class="container px-0">

        <letter-line
            v-for="line in lines"
            :ref="line.x1+'-'+line.y1+'-'+line.x2+'-'+line.y2"
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
            class="mb-3"
        >
            <b-col
                v-for="(col, y) in row"
                :key="y"
            >
                <letter
                    :ref="x+'-'+y"
                    :letter="board[x][y]"
                    @click="click(x, y)"
                    @submit="submit"
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
            attempt: [],
            solved: []
        }
    },
    computed: {
        attempted_word() {
            let str = ''

            this.attempt.forEach(([x,y]) => {
                str += this.board[x][y]
            })
            this.$emit('attempted-word', str)

            return str
        },
        lines() {
            let arr = []

            // For solved
            for (let i=0; i<this.solved.length; i++) {
                for (let j=0; j<this.solved[i].length-1; j++) {
                    arr.push(
                        {
                            x1: this.solved[i][j][0],
                            y1: this.solved[i][j][1],
                            x2: this.solved[i][j+1][0],
                            y2: this.solved[i][j+1][1]
                        }
                    )
                }
            }

            // For current attempt
            for (let i=0; i<this.attempt.length-1; i++) {
                arr.push(
                    {
                        x1: this.attempt[i][0],
                        y1: this.attempt[i][1],
                        x2: this.attempt[i+1][0],
                        y2: this.attempt[i+1][1]
                    }
                )
            }

            return arr
        }
    },
    methods: {
        click(x, y) {
            let reset_attempt = false

            // Not the first letter
            if(this.attempt.length != 0) {
                let prev_x = this.attempt[this.attempt.length-1][0]
                let prev_y = this.attempt[this.attempt.length-1][1]

                if([prev_x-1, prev_x, prev_x+1].includes(x))
                    if([prev_y-1, prev_y, prev_y+1].includes(y))
                        this.attempt.push([x, y])
                    else
                        reset_attempt = true
                else
                    reset_attempt = true
            }
            else
                this.attempt.push([x, y])

            if(reset_attempt) {
                this.reset_attempt()
                this.attempt = [ [x, y] ]
            }

            this.attempted_word; // force compute
        },
        submit() {
            // Check if correct guess
            if(JSON.stringify(this.strand_coordinates[this.attempted_word]) == JSON.stringify(this.attempt)) {
                this.solved.push(this.attempt)
                this.$emit('solved')
                this.attempt.forEach(([x,y]) => {
                    this.$refs[x+'-'+y][0].in_solved = true
                });
            }

            // Check if spangram
            if(this.spangram == this.attempted_word)
                this.mark_spangram()

            this.reset_attempt()

            // Check if game over
            if(this.solved.length == (Object.keys(this.strand_coordinates).length + 1)) {
                this.$toast('Good job!')
            }
        },
        reset_attempt() {
            this.attempt.forEach(([x,y]) => {
                this.$refs[x+'-'+y][0].selected = false
            });
            this.attempt = []
            this.attempted_word; // force compute
        },
        mark_spangram() {
            this.solved.push(this.attempt)

            for (let i=0; i<this.attempt.length-1; i++) {
                // First point
                let x1 = this.attempt[i][0]
                let y1 = this.attempt[i][1]

                // Second point
                let x2 = this.attempt[i+1][0]
                let y2 = this.attempt[i+1][1]

                // Mark points and connection as part of spangram
                this.$refs[x1+'-'+y1][0].in_spangram = true
                this.$refs[x2+'-'+y2][0].in_spangram = true
                this.$refs[x1+'-'+y1+'-'+x2+'-'+y2][0].in_spangram = true
            }

            this.$toast('Spangram!')
        }
    }
}
</script>
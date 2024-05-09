<template>
	<div class="container"  style="width: 300px !important;">
		<!-- Today's Theme -->
		<b-row class="w-100">
			<b-card
				class="theme w-100"
				no-footer
			>
				<template #header>
					<p>TODAY'S THEME</p>
				</template>
				<b-card-text>{{ clue }}</b-card-text>
			</b-card>
		</b-row>

		<!-- Current attempt -->
		<b-row
			class="mt-3 w-100 attempted_word"
			:key="attempted_word"
		>
			<h5 class="font-weight-bold">
				{{ attempted_word }}
			</h5>
		</b-row>

		<!-- Grid -->
		<b-row class="mt-2 w-100">
			<letter-grid
				ref="letter-grid"
				:board="board"
				:clue="clue"
				:spangram="spangram"
				:strands="strands"
				:strand_coordinates="strand_coordinates"
				:words="words"
				@attempted-word="(w) => attempted_word = w"
			/>
		</b-row>

		<!-- Buttons -->
		<b-row class="w-100"></b-row>
	</div>
</template>

<script>
import LetterGrid from './LetterGrid.vue'

export default {
	components: {
		LetterGrid
	},
	data() {
		return {
			board: [],
			clue: null,
			spangram: null,
			strands: [],
			strand_coordinates: [],
			words: [],

			attempted_word: null
		}
	},
	created() {
		// TODO - make dynamic
		let todays_data = require('./../assets/data/strands/63.json')

		this.board = todays_data.startingBoard
		this.clue = todays_data.clue
		this.spangram = todays_data.spangram
		this.strand_coordinates = todays_data.themeCoords
		this.strands = Object.keys(this.strand_coordinates)
		this.words = todays_data.solutions
	}
}
</script>
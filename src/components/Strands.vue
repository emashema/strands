<template>
	<div class="container"  style="width: 350px !important;">
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
				@word-found="words_found++"
				@solved="solved_count++"
			/>
		</b-row>

		<!-- Buttons -->
		<b-row class="mt-2 w-100" no-gutters>
			<b-col cols="auto">
				<div
					:class="{
						'btn': true,
						'btn-outline-secondary': true,
						'rounded-pill': true,
						'disabled': hint_disabled
					}"
					@click="$refs['letter-grid'].mark_hinted()"
				>Hint</div>
			</b-col>
			<b-col class="m-auto">
				<b>{{ solved_count }}</b> out of <b>{{ Object.keys(strand_coordinates).length+1 }}</b> theme words found.
			</b-col>
		</b-row>
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
			
			attempted_word: null,
			solved_count: 0,
			words_found: 0
		}
	},
	computed: {
		hint_disabled() {
			return this.words_found == 0 || this.words_found % 3 != 0
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
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

		<!-- Grid -->
		<b-row class="w-100 mt-4">
			<grid
				:board="board"
				:clue="clue"
				:spangram="spangram"
				:strands="strands"
				:strand_coordinates="strand_coordinates"
				:words="words"
			/>
		</b-row>

		<!-- Buttons -->
		<b-row class="w-100"></b-row>
	</div>
</template>

<script>
import Grid from './Grid.vue'

export default {
	components: {
		Grid
	},
	data() {
		return {
			solved: [],

			board: [],
			clue: null,
			spangram: null,
			strands: [],
			strand_coordinates: [],
			words: []
		}
	},
	created() {
		let todays_data = require('./../assets/data/strands/63.json')

		this.board = todays_data.startingBoard
		this.clue = todays_data.clue
		this.spangram = todays_data.spangram
		this.strand_coordinates = todays_data.themeCoords
		this.strands = this.strand_coordinates.keys()
		this.words = todays_data.solutions
	}
}
</script>
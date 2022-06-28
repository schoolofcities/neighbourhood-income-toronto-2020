<script>

	import Top from "./lib/TopSofC.svelte";
	import Map from "./lib/Map.svelte";
	import inc1961 from "./data/1961.geo.json";
	import inc1971 from "./data/1971.geo.json";
	import inc1981 from "./data/1981.geo.json";
	import inc1991 from "./data/1991.geo.json";
	import inc2001 from "./data/2001.geo.json";
	import inc2011 from "./data/2011.geo.json";


	let colours = ["#DC4633", "#ee9d78", "#e9e2c0", "#7eb4b3", "#007fa3"]
	let spacing = [50, 100, 150, 200, 250]

</script>


<Top />
<main>

	<div class="circles">
	  <svg>
		{#each [0,1,2,3,4] as d}
		  <circle cx={spacing[d]} cy="50%" r=5 fill={colours[d]} />
		{/each}
	  </svg>
	</div>
	
	<div class="title">
		<h1>Hello</h1>
	</div>

	
	<div class="mapBig">
		<Map year={"2011"}
		tracts={inc2011.features}/>
	</div>
	
	<div class="text">
		<p>For the six decades prior, clearly showing how lower-income neighbourhoods were once clustered in the centre.</p>
	</div>

	<div class="mapGrid">
		<div class="mapSmall">
			<Map year={"1961"} tracts={inc1961.features}/>
		</div>
		<div class="mapSmall">
			<Map year={"1971"} tracts={inc1971.features}/>
		</div>
		<div class="mapSmall">
			<Map year={"1981"} tracts={inc1981.features}/>
		</div><div class="mapSmall">
			<Map year={"1991"} tracts={inc1991.features}/>
		</div>
		<div class="mapSmall">
			<Map year={"2001"} tracts={inc2001.features}/>
		</div>
		<div class="mapSmall">
			<Map year={"2011"} tracts={inc2011.features}/>
		</div>
	</div>

</main>


<style>
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: #ffffff;
	}

	main {
		margin: 0 auto;
		width: 100%;
		max-width: 900px;
		position: relative;
	}

	.circles {
		margin: auto;
		max-width: 300px;
		height: 20px;
	}

	.title {
		margin: auto;
		max-width: 600px;
		width: 100%;
		margin-top: 70px;
	}

	.text {
		margin: auto;
		max-width: 600px;
		width: 100%;
	}

	.mapBig {
		margin: auto;
		max-width: 810px;
		border: solid 1px rgb(238, 238, 238);
		/* border-radius: 5px; */
		border-bottom-right-radius: 200px;
	}

	.mapGrid {
		margin: auto;
		max-width: 820px;
		width: 100%;
		display: grid;
		gap: 10px 10px;
		grid-template-columns: repeat(2, 1fr);
	}

	@media (max-width:820px) {
		.mapGrid {
			grid-template-columns: repeat(1, 1fr);
		}
	}

	.mapSmall {
		margin: auto;
		padding: -10px;
		max-width: 400px;
		border: solid 1px rgb(238, 238, 238);
		/* border-radius: 5px; */
		border-bottom-right-radius: 100px;
	}
	
</style>

<script>

	import Top from "./lib/TopSofC.svelte";
	import Map from "./lib/Map.svelte";
	import inc1961 from "./data/1961.geo.json";
	import inc1971 from "./data/1971.geo.json";
	import inc1981 from "./data/1981.geo.json";
</script>


<Top />
<main>
	
	<div class="title">
		<h1>Hello</h1>
	</div>
	<div class="mapBig">
		<Map year={"1961"}
		tracts={inc1961.features}/>
	</div>
	<div class="text">
		<p>Hello</p>
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

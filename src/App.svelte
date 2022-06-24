<script>

	import Top from "./lib/TopSofC.svelte";
	import Map from "./lib/Map.svelte";
	import inc1961 from "./data/1961.geo.json";
	import inc1971 from "./data/1971.geo.json";

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
	<div class="mapSmall">
		<b>1960</b>
		<Map year={"1961"} tracts={inc1961.features}/>
	</div>
	<div class="mapSmall">
		<b>1970</b>
		<Map year={"1971"} tracts={inc1971.features}/>
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
		background-color: rgb(255, 255, 255);
	}

	main {
		margin: 0 auto;
		width: 100%;
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
		max-width: 800px;
		border: solid 1px rgb(243, 232, 232);
		/* border-radius: 5px; */
		border-bottom-right-radius: 200px;
	}

	.mapSmall {
		margin: auto;
		max-width: 400px;
		border: solid 1px rgb(243, 232, 232);
		/* border-radius: 5px; */
		border-bottom-right-radius: 100px;
	}
	
</style>

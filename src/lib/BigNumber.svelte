<script>

	export var number;
	export var label;
	export var type;

	$: colour = "black";	
	$: type ? colour = "black" : colour = "rgb(66, 66, 66)";

</script>

<div class="big-number" style="color:{colour}">
	<div class="big-number-number">{number}</div>
	<div class="big-number-label">{label}</div>
</div>

<style>
	.big-number {
		overflow: hidden;
		padding-top: 8px;
		width: 280px;
		margin-bottom: -5px;
	}
	.big-number-number {
		float: left;
		width: 90px;
		font-family: "Source Serif Pro", serif;
		font-size: 22px;
		text-align: right;
		padding-right: 5px;
	}
	.big-number-label {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		font-size: 13px;
		text-align: left;
		padding: 5px;
	}
</style>

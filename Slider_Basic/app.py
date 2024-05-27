from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("Hello Faith!"),
    ui.input_slider("n", "N", 0, 100, 25),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

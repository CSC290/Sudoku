package application;
	
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.geometry.Pos;


public class Main extends Application {
	@Override
	public void start(Stage stage) {
		BorderPane border = new BorderPane();
		VBox menu = new VBox(10);
		menu.setAlignment(Pos.CENTER);
		
		
		Label title = new Label("Sudoku");
		menu.getChildren().add(title);
		
		Button start = new Button("START");
		menu.getChildren().add(start);
		
		Button settings = new Button("SETTINGS");
		menu.getChildren().add(settings);
		
		border.setCenter(menu);
		
		Scene scene = new Scene(border);
		
		stage.setTitle("SUDOKU");
		stage.setScene(scene);
		
		stage.show();
		
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}

import java.util.HashMap;
import java.util.Scanner;

public class SimpleChatbot {
    public static void main(String[] args) {
        
        // Create HashMap to store questions and responses
        HashMap<String, String> bot = new HashMap<>();
        
        // Add responses using put()
        bot.put("hello", "Hi there!");
        bot.put("how are you", "I'm just code, but I'm doing great!");
        bot.put("what is your name", "I am a simple Java chatbot.");
        bot.put("bye", "Goodbye! Have a nice day.");

        Scanner sc = new Scanner(System.in);
        String userInput;

        System.out.println("Chatbot started! Type 'bye' to exit.");

        while (true) {
            System.out.print("You: ");
            userInput = sc.nextLine().toLowerCase();

            // Exit condition
            if (userInput.equals("bye")) {
                System.out.println("Bot: " + bot.get("bye"));
                break;
            }

            // Get response using get()
            String response = bot.get(userInput);

            if (response != null) {
                System.out.println("Bot: " + response);
            } else {
                System.out.println("Bot: Sorry, I don't understand that.");
            }
        }

        sc.close();
    }
}

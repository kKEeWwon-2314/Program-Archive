public class Unit9Animal {
    private boolean vertebrate;
    private String hairColor;

    // Encapsulation
    public boolean getVertebrate() {
        return vertebrate;
    }
    public String getHairColor() {
        return hairColor;
    }

    public void Mammal() {
        vertebrate = true;
    }
    public void Mammal(String hairColor) {
        vertebrate = true;
        this.hairColor = hairColor;
    }
    public void Mammal(String hairColor, boolean isVertebrate) {
        vertebrate = isVertebrate;
        this.hairColor = hairColor;
    }
}

public class StepTracker {
    public int totalDays;
    public int activeDays;
    public int totalSteps;

    public int minStepsActive;

    // Initialize variables
    public StepTracker(int minStepsActive)
    {
        totalDays = 0;
        activeDays = 0;
        totalSteps = 0;

        this.minStepsActive = minStepsActive;
    }

    public int activeDays() 
    {
        return activeDays();
    }

    public double averageSteps() 
    {
        if (totalDays == 0)
        {
            return 0;
        }

        return totalSteps / totalDays;
    }

    public void addDailySteps(int steps)
    {
        if (steps >= minStepsActive)
        {
            activeDays++;
        } 

        totalDays++;
        totalSteps += steps;
    }

    // Exectute main method
    public static void main(String[] args)
    {
        StepTracker tr = new StepTracker(10000);

        tr.addDailySteps(2001);
        tr.addDailySteps(2);

        System.out.println(tr.averageSteps());
    }
}
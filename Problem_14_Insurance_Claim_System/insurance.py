print("====================================")
print(" Insurance Claim Decision System ")
print("====================================")

policy_active = input("Is Policy Active? (yes/no): ").lower()
documents_valid = input("Are Documents Valid? (yes/no): ").lower()
accident_reported = input("Was Accident Reported? (yes/no): ").lower()

print("\nChecking Rules...\n")

if (
    policy_active == "yes"
    and documents_valid == "yes"
    and accident_reported == "yes"
):
    print("Rule Applied:")
    print("Policy Active AND Documents Valid AND Accident Reported = TRUE")
    print("\nFinal Decision:")
    print("Claim Approved")
else:
    print("Rule Applied:")
    print("One or more conditions are FALSE")
    print("\nFinal Decision:")
    print("Claim Rejected")
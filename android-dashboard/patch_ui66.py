from pathlib import Path
import base64

ROOT = Path("FYT-Launcher-Mod")
LAUNCHER = ROOT / "app/src/main/java/com/android/launcher66/Launcher.java"
B64 = Path("android-dashboard/approved_bg.b64")

# Install approved TAKI HOUSE background into every density bucket used by Launcher66.
bg = base64.b64decode(B64.read_text().strip())
for p in (ROOT / "app/src/main/res").glob("drawable-*/def_bg.webp"):
    p.write_bytes(bg)
for p in (ROOT / "app/src/main/res").glob("drawable-*/def_bg_n.webp"):
    p.write_bytes(bg)

s = LAUNCHER.read_text()

# Import GradientDrawable for the speed HUD card.
needle = "import android.graphics.drawable.Drawable;\n"
if "import android.graphics.drawable.GradientDrawable;" not in s:
    s = s.replace(needle, needle + "import android.graphics.drawable.GradientDrawable;\n", 1)

# Add a TAKI speed TextView field.
needle = "    private TextView mTvSpeed;\n"
if "private TextView takiSpeedView;" not in s:
    s = s.replace(needle, needle + "    private TextView takiSpeedView;\n", 1)

# Initialise the overlay after launcher root/workspace are available.
needle = "        mWorkspace = (Workspace) mDragLayer.findViewById(R.id.workspace);\n"
if "initTakiSpeedOverlay();" not in s:
    s = s.replace(needle, needle + "        initTakiSpeedOverlay();\n", 1)

# Feed CANBUS speed into the TAKI overlay.
needle = "                    Launcher.this.carSpeed = ints[0];\n"
if "Launcher.this.updateTakiSpeed(Launcher.this.carSpeed);" not in s:
    s = s.replace(
        "                    if (Launcher.this.carSpeed == 1) {\n                        Launcher.this.carSpeed = 0;\n                    }\n",
        "                    if (Launcher.this.carSpeed == 1) {\n                        Launcher.this.carSpeed = 0;\n                    }\n                    Launcher.this.updateTakiSpeed(Launcher.this.carSpeed);\n",
        1
    )

# Feed navigation speed as a second source when available.
needle = '                mCurSpeedView.setText(String.valueOf(MyAutoMapReceiver.mCurSpeed) + "km/h");\n'
if "updateTakiSpeed(MyAutoMapReceiver.mCurSpeed);" not in s:
    s = s.replace(needle, needle + "                updateTakiSpeed(MyAutoMapReceiver.mCurSpeed);\n", 1)

# Add overlay helpers immediately before setupViews().
marker = "    private void setupViews() {\n"
if "private void initTakiSpeedOverlay()" not in s:
    methods = r'''
    private void initTakiSpeedOverlay() {
        if (!(mLauncherView instanceof FrameLayout)) {
            return;
        }
        if (takiSpeedView != null && takiSpeedView.getParent() != null) {
            return;
        }

        takiSpeedView = new TextView(this);
        takiSpeedView.setGravity(Gravity.CENTER);
        takiSpeedView.setTextColor(Color.WHITE);
        takiSpeedView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 54);
        takiSpeedView.setTypeface(android.graphics.Typeface.create("sans-serif-light", android.graphics.Typeface.NORMAL));
        takiSpeedView.setIncludeFontPadding(false);
        takiSpeedView.setClickable(false);
        takiSpeedView.setFocusable(false);
        takiSpeedView.setElevation(30f);

        GradientDrawable bg = new GradientDrawable();
        bg.setColor(Color.argb(205, 15, 46, 88));
        bg.setCornerRadius(32f);
        bg.setStroke(2, Color.argb(175, 35, 196, 255));
        takiSpeedView.setBackground(bg);

        int width = (int) (LauncherApplication.getScreenWidth() * 0.20f);
        int height = (int) (LauncherApplication.getScreenHeight() * 0.18f);
        FrameLayout.LayoutParams lp = new FrameLayout.LayoutParams(width, height, Gravity.TOP | Gravity.CENTER_HORIZONTAL);
        lp.topMargin = (int) (LauncherApplication.getScreenHeight() * 0.018f);
        ((FrameLayout) mLauncherView).addView(takiSpeedView, lp);
        updateTakiSpeed(0);
    }

    private void updateTakiSpeed(int speed) {
        if (takiSpeedView == null) {
            return;
        }
        int safeSpeed = Math.max(0, Math.min(speed, 260));
        String text = safeSpeed + "\nkm/h";
        SpannableString styled = new SpannableString(text);
        int unitStart = text.indexOf("\n") + 1;
        if (unitStart > 0 && unitStart < text.length()) {
            styled.setSpan(new RelativeSizeSpan(0.38f), unitStart, text.length(), 0);
        }
        takiSpeedView.setText(styled);
    }

'''
    s = s.replace(marker, methods + marker, 1)

LAUNCHER.write_text(s)
print("TAKI UI66 patch applied")

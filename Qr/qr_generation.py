import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer,VerticalBarsDrawer,HorizontalBarsDrawer

from qrcode.image.styles.colormasks import RadialGradiantColorMask,VerticalGradiantColorMask,HorizontalGradiantColorMask,SquareGradiantColorMask , ImageColorMask


qr_code = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,)
qr_code.add_data("himan_delbina")
qr_code.make(fit=True)


qr_code_generate = qr_code.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    # module_drawer=RoundedModuleDrawer(radius_ratio=0.6),
    eye_drawer=RoundedModuleDrawer(radius_ratio=0.6),
    color_mask=RadialGradiantColorMask(back_color=(255,255,255),edge_color=(0,0,0),center_color=(0,17,255))
    # color_mask=SquareGradiantColorMask(back_color=(255,255,255),edge_color=(0,0,0),center_color=(255,100,100))
    # color_mask=HorizontalGradiantColorMask(back_color=(255,255,255),left_color=(0,0,0),right_color=(255,100,100))
    # color_mask=VerticalGradiantColorMask(back_color=(255,255,255),top_color=(0,0,0),bottom_color=(255,100,100))
    )


qr_code_generate.save('qr.png')